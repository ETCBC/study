![etcbc-data](https://raw.github.com/judithgottschalk/ETCBC-data/master/images/VU-ETCBC-small.png)

IPython notebooks developed for the study of the Hebrew Bible.

Designed to work together with
[LAF-Fabric](http://laf-fabric.readthedocs.org/en/latest/).

In order to run these notebooks, you need also:

* [LAF-Fabric](https://github.com/dirkroorda/laf-fabric)
* the LAF version of the Hebrew Bible (not yet freely available, consult [Dirk Roorda](dirk.roorda@dans.knaw.nl)

N.B.:

The configuration file script is *laf-fabric-sample.cfg* in the directory *notebooks*.
You have to copy this to *laf-fabric.cfg* in every notebook subdirectory and make your changes there.
The files *laf-fabric.cfg* will not be distributed. This will help you to keep your
installation up to date.

In it there is just one setting, and you have to adapt it to your local situation:

    [locations]
    work_dir  = /Users/dirk/Scratch/shebanq/results
    
*work_dir* is folder where all the data is, input, intermediate, and output.


