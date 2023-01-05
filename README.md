# bricks
A Python OpenCV solution to the bricks counting problem.

## Problem Description
The aim is to accurately count the number of bricks in a photograph.


## Algorithm Steps
- Convert the image to grayscale
- Blur the image using a Gaussian filter
- Threshold the image using adaptive thresholding and a Gaussian kernel
- Remove minor artifacts by identifying and filling small contours
- Erode the image using a kernel of size 19x19 with initial values of -5
- Find contours in the eroded image

#### Grayscaling
  Grayscaling is performed to reduce the image to a single dimension and make calculations faster and easier. The default OpenCV `CV.COLOR_BGR2GRAY` function is used for this step.
  
#### Blurring
  A Gaussian blur with a kernel size of 9x9 is applied to improve the accuracy of contour-finding algorithms.
  
#### Thresholding
  After grayscaling and blurring, adaptive thresholding is applied using a Gaussian kernel with a size of 21x21 and a constant of 3. This step significantly improves the ability to identify separate objects in the image.
  
![thresh_Bricks_1](https://user-images.githubusercontent.com/78561567/193474881-abca9091-0072-45ac-a959-587c3f161b55.jpg)
![thresh_Bricks_2](https://user-images.githubusercontent.com/78561567/193474882-c7d35d4e-5584-4f63-bf78-33e90e8cf1a3.jpg)
![thresh_Bricks_3](https://user-images.githubusercontent.com/78561567/193474876-6f2a340b-d5cf-4851-886b-80cef0afdc5f.jpg)
![thresh_Bricks_4](https://user-images.githubusercontent.com/78561567/193474884-0044a157-e3f4-4216-a707-fd59197ba9cf.jpg)

#### Removing minor artifacts
  In order to reduce the number of falsely identified bricks after erosion, minor artifacts are removed by finding contours in the thresholded image and filling the smallest with white. This step significantly reduces the number of artifacts.
  
  ![thresh_Bricks_1](https://user-images.githubusercontent.com/78561567/193475116-a58ede47-0879-4fbb-b5f3-75d13394561b.jpg)
![thresh_Bricks_2](https://user-images.githubusercontent.com/78561567/193475118-a12ceaf3-29dd-4e90-a9fb-1deae37de313.jpg)
![thresh_Bricks_3](https://user-images.githubusercontent.com/78561567/193475119-0dd1cb33-a29d-454c-bb19-b800380efba7.jpg)
![thresh_Bricks_4](https://user-images.githubusercontent.com/78561567/193475121-752334bb-4a03-4fe4-a9b3-5f2ac161c9fc.jpg)


#### Eroding
  The main problem left after the thresholding is applied are the bricks with identical colour 'glued' together. To fix this, we will apply eroding with the kernel of size 19x19 and initial values at -5. After the image is eroded, the amount of 'glued' bricks significantly reduces.
  
  While this method gives an accurate result, sometimes it can have a noticeable error in the case of small-sized bricks which are fully destroyed with the erosion. This case is checked separately and the smaller sized erosion kernel 3x3 is applied. (More formally, we check if the number of contours is significantly reduced).
  
![thresh_Bricks_1](https://user-images.githubusercontent.com/78561567/193475236-a8673b99-d319-47f0-909c-a64bd646e7de.jpg)
![thresh_Bricks_2](https://user-images.githubusercontent.com/78561567/193475238-1797f709-ba1c-4014-b98a-bc94e2ba451a.jpg)
![thresh_Bricks_3](https://user-images.githubusercontent.com/78561567/193475240-7263641b-780d-4ac9-9ff1-1d8b8ec690d5.jpg)
![thresh_Bricks_4](https://user-images.githubusercontent.com/78561567/193475241-c14c1544-6e6d-4e96-bdf2-5d69727bc6da.jpg)

#### Finding Contours
  After the image has been eroded, contours are found in the image. This allows for a final count of the number of bricks.

![thresh_Bricks_1](https://user-images.githubusercontent.com/78561567/193475331-1a3efa5a-47e0-450f-a6ae-1e0034c38e3f.jpg)
![thresh_Bricks_2](https://user-images.githubusercontent.com/78561567/193475334-2123a4ed-b5ac-4d1d-aead-f284b0e7d945.jpg)
![thresh_Bricks_3](https://user-images.githubusercontent.com/78561567/193475336-c6cf4519-5080-4447-a3c6-d2ce846ca760.jpg)
![thresh_Bricks_4](https://user-images.githubusercontent.com/78561567/193475338-7aa3e881-c00c-4da2-8332-909581b17f00.jpg)

Given approach gives satisfying accuracy ~0.94 and processes given images in 584 millis.


## Results

The algorithm has been shown to accurately count bricks with a high degree of precision. It is able to effectively handle cases where bricks are partially obscured or "glued" together.

## Usage

To use the script, first download it and navigate to the directory containing the script in your terminal. Then, run `python3 main.py`. The script will process every image located in the `./images` folder and output the number of bricks detected in each image. The modified images with green dots indicating the detected bricks will be saved in the `./res` folder.
