import sys
import collections
from copy import deepcopy

class FeatureDoc(object):

    def __init__(self, processor, baseload, study):
        self.processor = processor
        self.study = study
        this_load = deepcopy(baseload)
        this_load['features']['shebanq']['node'].extend(['ft.{}'.format(x) for x in study['features']])
        processor.init('bhs3.txt.hdr', '--', 'feature-doc', this_load)
        self.API = processor.API()

    def feature_doc(self):
        msg = self.API['msg']
        outfile = self.API['outfile']
        F = self.API['F']
        NN = self.API['NN']
        msg = self.API['msg']
        outfile = self.API['outfile']
        my_file = self.API['my_file']

        msg("Looking up feature values ... ")
        feats = [(ft, "shebanq_ft_{}".format(ft)) for ft in self.study['features']]
        absence_values = self.study['absence_values']
        VALUE_THRESHOLD = self.study['VALUE_THRESHOLD']

# values and object types for this feature
        
        vals_def = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
        vals_undef = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
        n_otypes = collections.defaultdict(lambda: collections.defaultdict(lambda: [0,0]))
        n_otypesi = collections.defaultdict(lambda: collections.defaultdict(lambda: [0,0]))
        
        for node in NN():
            for (ft, feat) in feats:
                val = F.F[feat].v(node)
                otype = F.shebanq_db_otype.v(node)
                if val != None:
                    if val in absence_values:
                        n_otypes[otype][ft][0] += 1
                        n_otypesi[ft][otype][0] += 1
                        vals_undef[ft][val] += 1
                    else:
                        n_otypes[otype][ft][1] += 1
                        n_otypesi[ft][otype][1] += 1
                        vals_def[ft][val] += 1
        
        otypes = sorted(n_otypes.keys())

        msg("Computing results ...")
        
        for (ft, feat) in feats:
            result_file = outfile("{} values.txt".format(ft))
            result_file.write("UNDEFINED VALUES\n")
            for x in sorted(vals_undef[ft].items(), key=lambda y: (-y[1], y[0])):
                result_file.write("{} x {}\n".format(*x))
            result_file.write("\nDEFINED VALUES\n")
            for x in sorted(vals_def[ft].items(), key=lambda y: (-y[1], y[0])):
                result_file.write("{} x {}\n".format(*x))
            result_file.close()
        
        result_file = outfile("types.txt")
        for ft in sorted(n_otypesi):
            for otype in sorted(n_otypesi[ft]):
                result_file.write("{}\t{}\t{}\t{}\n".format(ft, otype, *n_otypesi[ft][otype]))
        result_file.close()
        
        n_vals_def = collections.defaultdict(lambda: 0)
        n_vals_undef = collections.defaultdict(lambda: 0)
        for (ft, feat) in feats:
            for val in vals_def[ft]:
                n_vals_def[ft] += vals_def[ft][val]
            for val in vals_undef[ft]:
                n_vals_undef[ft] += vals_undef[ft][val]
        
        summary_file = outfile("summary.txt")
        summary_file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
            'Feature',
            'val (-)',
            'val (+)',
            '#vals (-)',
            '#vals (+)',
            'occs (-)',
            'occs (+)',
            '\t'.join(["{} (-)\t{} (+)".format(otype, otype) for otype in otypes]),
        ))
                           
        for (ft, feat) in feats:
            summary_file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                ft,
                '',
                '',
                len(vals_undef[ft]),
                len(vals_def[ft]),
                n_vals_undef[ft],
                n_vals_def[ft],
                '\t'.join(["{}\t{}".format(*n_otypes[otype][ft]) for otype in otypes]),
            ))
            for (val, n) in sorted(vals_undef[ft].items(), key=lambda x: (-x[1], x[0])):
                summary_file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                    '',
                    val,
                    '',
                    n,
                    '',
                    '',
                    '',
                    '\t' * (2 * len(otypes) - 1),
            ))
            i = 0
            for (val, n) in sorted(vals_def[ft].items(), key=lambda x: (-x[1], x[0])):
                i += 1
                if i > VALUE_THRESHOLD:
                    summary_file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                        '',
                        '',
                        "{} MORE".format(len(vals_def[ft]) - VALUE_THRESHOLD),
                        '',
                        '',
                        '',
                        '',
                        '\t' * (2 * len(otypes) - 1),
                    ))
                    break
                summary_file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                    '',
                    '',
                    val,
                    '',
                    n,
                    '',
                    '',
                    '\t' * (2 * len(otypes) - 1),
            ))
        summary_file.close()
        
        msg("Done")
