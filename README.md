![etcbc-data](https://raw.github.com/judithgottschalk/ETCBC-data/master/images/VU-ETCBC-small.png)
![laf-fabric](https://raw.github.com/judithgottschalk/ETCBC-data/master/images/laf-fabric-small.png)

IPython notebooks developed for the study of the Hebrew Bible.

Designed to work together with
[LAF-Fabric](http://laf-fabric.readthedocs.org/en/latest/).

In order to run these notebooks, you need:

* download/clone [LAF-Fabric](https://github.com/dirkroorda/laf-fabric)
* the compiled LAF version of the Hebrew Bible: [download](https://www.dropbox.com/s/1oqvb92sqn7vuml/laf-fabric-data.zip)
  (this is a paasword protected zip file of 160 MB, ask [Dirk Roorda](dirk.roorda@dans.knaw.nl) for the password.

N.B.:

The configuration file script is *laf-fabric-sample.cfg* in the directory *notebooks*.
You have to copy this to *laf-fabric.cfg* in every notebook subdirectory and make your changes there.
The files *laf-fabric.cfg* will not be distributed. This will help you to keep your
installation up to date.

In it there are just one or two settings, and you have to adapt it to your local situation:

    [locations]
    work_dir  = /Users/you/laf-data-dir
    #laf-dir  = /Users/you/shebanq/results/laf
    
*work_dir* is folder where all the data is, input, intermediate, and output.
*laf_dir* is the folder where the original laf-xml data is. Optional. LAF-Fabric can work without it.

# Table of notebooks

## Annotating
Making your own annotation and add them to the data for new analysis.

[annox_workflow](http://nbviewer.ipython.org/github/judithgottschalk/ETCBC-data/blob/master/notebooks/annotating/annox_workflow.ipynb)


