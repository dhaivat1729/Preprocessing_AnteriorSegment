                       Preprocessing of Cow EYE images

    What is this repository about?
    ------------------------------

        This repository has raw images, pre-processed images, preprocessing codes and some intermediate components used inside the code.


    What files/folders does it have?
    --------------------------------

        This repository has two directories, Left and right.

        1. Left: This directory has all the data acquired from left camera, and all the codes and files related to processing of raw data of right camera only.

        1. right: This directory has all the data acquired from right camera, and all the codes and files related to processing of raw data from right camera only.

        Both directories have certain sub-directories and files:

        Directories:
        ------------

        1. raw_images: raw images captured from camera system are saved inside this directory.

        2. Not_processed_images: This folder has all those extracted images which are not processed even after running preprocessing algorithm.

        3. Final_images: All the preprocessed images are saved inside this directory.

        Files:
        ------

        1. Mask.png: This is an image file which is used during preprocessing.

        2. Preprocessing.py: This is main python code which is implementation of preprocessing algorithm.

        3. ProcessingNotprocessedimages.py: This code should be executed after running Preprocessing algorithm on raw data. It processes those images which are not processed 		    properly after applying preprocessing algorithm.

    Dependencies:
    -----------------

        1. python 2.7 or above
        2. Numpy, Scipy ( Python modules )
        3. SimpleCV ( Computer vision python framework )
        4. OpenCV ( Computer vision framework )

    About code:
    --------------

        1. Preprocessing.py: This code should be executed first.

        2. ProcessingNotprocessedimages.py: This code should not be executed without executing Preprocessing.py and this code should be executed only after executing 									  Preprocessing algorithm.

    How to run the code:
    -------------------------

        Suppose if we want to execute preprocessing algorithm for data acquired from left camera, do the following:
	--------------------------------------------------------------------------------------------------------------------------------

        cd ../../Preprocessing_AnteriorSegment/Left

        python Preprocessing.py

        python ProcessingNotprocessedimages.py

        That's it. You can check your Final_images directory inside your Left directory of Repository.

        Suppose if we want to execute preprocessing algorithm for data acquired from right camera, do the following:
	----------------------------------------------------------------------------------------------------------------------------------

        cd ../../Preprocessing_AnteriorSegment/right

        python Preprocessing.py

        python ProcessingNotprocessedimages.py
