# Image Duplicate Finder

## Overview

This Python project aims to efficiently compare large datasets of images to identify duplicates. The user can specify various actions to take with the duplicates, such as saving them to a text file, moving them to a separate folder, or deleting them altogether. The pipeline involves several stages including user input, discovery, comparison, and result generation.

## Pipeline

### 1. User Input

The user provides input specifying the dataset and desired actions for handling duplicates.

### 2. Discovery

The program scans the dataset to identify all images and their locations.

### 3. Comparison

#### 3.1. Meta Data Comparison

Metadata of the images, such as size, date, and camera information, are compared. If the metadata is the same, no further comparisons need to be made. This is however the users to decide should they want to go for a deep scan.

#### 3.3. Image Preprocessing

If the metadata is not identical, preprocessing steps are applied to standardize the images:
- Rotation to the same orientation. (To detect rotated images)
- Compression to reduce size. (To tackle different resolutions of the same image.)

#### 3.4. Pixel Comparison

- A subset of pixels is selected for comparison, typically a user-defined area (e.g., 10% of image dimensions by default).
- All pixels in the selected area are compared for similarity.
- If the subsets are the same, it now constitutes a full image comparison; otherwise, the images at hand can be considered different.

### 4. Result

The program generates a report indicating which images are duplicates based on the specified criteria. The user can then choose to save this list to a text file, move the duplicates to a separate folder, or delete them.

## Configuration

- Adjust comparison parameters such as the percentage of image dimensions for pixel comparison.
- Modify actions to be taken with duplicates (e.g., save to text file, move to folder, delete).

## Contributing

Contributions are welcome! Feel free to fork the project and submit pull requests for any improvements or new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.