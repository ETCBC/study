![etcbc-data](https://raw.github.com/judithgottschalk/ETCBC-data/master/images/VU-ETCBC-small.png)
![laf-fabric](https://raw.github.com/judithgottschalk/ETCBC-data/master/images/laf-fabric-small.png)

IPython notebooks developed for the study of the Hebrew Bible.

# Table of notebooks

## Annotating
Making your own annotation and add them to the data for new analysis.

* [annox_workflow](http://nbviewer.ipython.org/github/judithgottschalk/ETCBC-data/blob/master/notebooks/annotating/annox_workflow.ipynb)

## Feature Studies
Explorations into the features in the ETCBC text database of the Hebrew Bible.

*Feature-Doc* below is a generic instrument to create a statistical overview of defined and undefined values of features selected by you.
Here you can also find the list of all available features.

The other notebooks contain descriptions of the meanings of certain features and their values,
and they will show you examples, and they will test assertions about them.
For example: *the ``clause_constituent_relation``-feature has value ``none`` for a node if and only if that node has no outgoing edges labeled ``mother``*.

* [feature-doc](https://github.com/judithgottschalk/ETCBC-data/blob/master/notebooks/feature-studies/feature-doc.ipynb)
* [clause_atoms](http://nbviewer.ipython.org/github/judithgottschalk/ETCBC-data/blob/master/notebooks/feature-studies/clause_atoms.ipynb)
* [clause_phrase_types](http://nbviewer.ipython.org/github/judithgottschalk/ETCBC-data/blob/master/notebooks/feature-studies/clause_phrase_types.ipynb)
* [tense](http://nbviewer.ipython.org/github/judithgottschalk/ETCBC-data/blob/master/notebooks/feature-studies/Tense.ipynb)

# Linguistic Variation
Research into linguistic variation in the Hebrew Bible books.
Datamining, statistics, visualization.

* [cooccurrences](http://nbviewer.ipython.org/github/judithgottschalk/ETCBC-data/blob/master/notebooks/language-variation/cooccurrences.ipynb)

## Syntax
Research to syntactic phenomena in the sentences of the Hebrew Bible.
Tree construction.
Correlating morphological features to syntactic functions.

* [trees](http://nbviewer.ipython.org/github/judithgottschalk/ETCBC-data/blob/master/notebooks/syntax/trees.ipynb)
* [participle](http://nbviewer.ipython.org/github/judithgottschalk/ETCBC-data/blob/master/notebooks/syntax/participle.ipynb)

# Getting started
In order to run these notebooks, you need:

* download/clone [LAF-Fabric](https://github.com/dirkroorda/laf-fabric)
* read some documentation [LAF-Fabric](http://laf-fabric.readthedocs.org/en/latest/)
* [download](https://www.dropbox.com/s/1oqvb92sqn7vuml/laf-fabric-data.zip) the compiled LAF version of the Hebrew Bible
  (this is a password protected zip file of ~ 150 MB, ask [Dirk Roorda](dirk.roorda@dans.knaw.nl) for the password).
* configure your notebook directories.

## Configuration
In every notebook subdirectory you need (the same) configuration file called *laf-fabric.cfg*.
Make copies from the *laf-fabric-sample.cfg* in the *notebooks* directory and modify the one relevant setting in it.
The files *laf-fabric.cfg* will not be distributed, so they will not be overwritten when you clone new versions.
This will help you to keep your installation up to date.

In *laf-fabric.cfg* it there are just one or two settings, and you have to adapt it to your local situation:

    [locations]
    work_dir  = /Users/you/laf-data-dir
    #laf-dir  = /Users/you/shebanq/results/laf
    
*work_dir* is folder where all the data is, input, intermediate, and output.

*laf_dir* is the folder where the original laf-xml data is.
It is *optional*. LAF-Fabric can work without it.
If you do not have the original LAF source, leave it commented out.

