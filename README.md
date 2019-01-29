# rfeldhans-MA-master
Master repository for my master thesis. Contains documentation and links to all parts of the thesis.

# Thesis text
The repository containing the latex source files (and a .pdf) can be found [here](https://github.com/Slothologist/MasterThesis).

# Wiki 
Additional information/ requirements may be found in [this repositories wiki](https://github.com/Slothologist/MA-master/wiki).
In detail, there can be found...
- [User stories](https://github.com/Slothologist/MA-master/wiki/User-stories) 
- [A list of the features of the pipeline](https://github.com/Slothologist/MA-master/wiki/Features---comparison)

# Code
The main repository for the library can be found [here](https://github.com/Slothologist/esiaf_ros).
It contains the library used to connect the nodes of the pipeline as well as essential nodes, such as the Orchestrator, which controls the audio flow and node connections;
and other basic nodes, such as nodes for grabbing and playing back audio.

Other nodes can be found as follows:

#### Voice activation detection  

- The audio segmenter can be found [here](https://github.com/Slothologist/AudioSegmenter) and mainly contains a reimplementation of the double threshold decibel based voice activation detection found in the [PocketsphinxAdapter](https://projects.cit-ec.uni-bielefeld.de/projects/ps-adapter).


#### Speech recognition

- A Deepspeech node can be found [here](https://github.com/Slothologist/DeepSpeech4Ros).

# Additional notes

Additional, work in progress, notes can be found in a google-doc [here](https://docs.google.com/document/d/1G3bQSCIhKrKovwQ59vWOCoCpVycuWBH9_QjeYPbvero/edit?usp=sharing).
Some information may double with the latex document or the wiki.
