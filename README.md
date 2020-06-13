# VRAI-Dataset
The VRAI Vehicle Re-identification Dataset

Our VRAI is released now！<br>

Thanks for your interest in our VRAI dataset.<br>

Our VRAI dataset is used for Vehicle Re-identification research in aerial imagery. With the rapid development of the Unmanned Aerial Vehicles (UAVs), the UAV-based vision applications have been drawing an increasing attentions from both industry and academia. However, the UAV-based vehicle reidentiﬁcation is rarely studied, although it has a variety of potential applications such as long-term tracking, visual object retrieval, etc. One of the reasons is the lack of the corresponding publicly available dataset, which will take a large amount of human efforts for UAV ﬂying, video capture and data annotation. In this case, we collect and release our VRAI to support in-depth research.<br>


## Dataset partition:


The VARI dataset is split to the training set and testing set, among which the training set contains 66,113 images with 6,302 IDs, and the test set contains 71,500 images with 6,720 IDs. Besides, we subsample a subset from the testing set as the validation set. The validation set contains 10% images of testing set.<br>

## Annotation:

### Trainng set:
    Image name: ID_Cam_Frame.jpg, such as 0000000X_000Y_0000000Z.jpg, the 0000000X indicates this image belongs to ID No.X, the 000Y indicates this image is captured by camera Y and 0000000z indicates this image is the Z th frame in this trajectory.
    Annotation files: train_annotation.pkl
                      train_im_names: The File Names of images in the training set.
                      color_label: A dictionary to store the mapping from IDs to Vehicle Color Labels.
                      type_label: A dictionary to store the mapping from IDs to Vehicle Type Labels.
                      bumper_label & wheel_label & sky_label & luggage_label: A dictionary to store the mapping from IDs to Vehicle Attributes.
                      keypoint_label: A dictionary to store the mapping from Image Names to Vehicle Discriminative Parts Bounding Boxes.
### Validation set:
    Image name: Random_string_Cams.jpg, such as 00AV11D2_C1.jpg, the 00AV11D2 is a random string and the C1 indicates image is captured by camera 1.
    Annotation files: val_annotation.pkl
                      val_im_names: The File Names of images in the Validation set.
                      color_label: A dictionary to store the mapping from Image Names to Vehicle Color Labels.
                      type_label: A dictionary to store the mapping from Image Names to Vehicle Type Labels.
                      bumper_label & wheel_label & sky_label & luggage_label: A dictionary to store the mapping from Image Names to Vehicle Attributes.
                      keypoint_label: A dictionary to store the mapping from Image Names to Vehicle Discriminative Parts Bounding Boxes.
                      val_gallery_order: A list to store Image Names in gallery set. It also reflects the Serial Number of gallery images.
                      val_query_order: A list to store Image Names in query set. It also reflects the Serial Number of query images.
### Testing set:
    Image name: Random_string_Cams.jpg such as 00AV11D2_C1.jpg, the 00AV11D2 is a random string and the C1 indicates this image is captured by camera 1.
    Annotation files: test_annotation.pkl
                      test_im_names: The File Names of images in the testing set.
                      color_label: A dictionary to store the mapping from Image Names to Vehicle Color Labels.
                      type_label: A dictionary to store the mapping from Image Names to Vehicle Type Labels.
                      bumper_label: & wheel_label & sky_label & luggage_label A dictionary to store the mapping from Image Names to Vehicle Attributes. 
                      keypoint_label: A dictionary to store the mapping from Image Names to Vehicle Discriminative Parts Bounding Boxes. 
                      test_gallery_order: A list to store Image Names in gallery set. It also reflects the Serial Number of gallery images. 
                      test_query_order: A list to store Image Names in query set. It also reflects the Serial Number of query images. 
            
            
## Evaluation Metrics:

We adopt the popular mean Average Precision (mAP) and Cumulative Matching Cure (CMC) as in other ReID works. Besides, we host a challenge in Evalai. You can test the performance on our VRAI through this challenge.<br>

We provide an example submission submission_t.json here.

Google Drive:
<a href='https://drive.google.com/drive/folders/1nsxZjrGvO1wfqas_rWTd9TxCeMyLWqMm?usp=sharing'>Google</a>

Baiduyun:
<a href='https://drive.google.com/drive/folders/1nsxZjrGvO1wfqas_rWTd9TxCeMyLWqMm?usp=sharing'>Baiduyun</a>



