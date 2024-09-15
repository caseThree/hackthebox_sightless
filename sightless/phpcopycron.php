<?php
// Define the source and destination paths
$source = '/root/root.txt';
$destination = '/home/michael/root.txt';

// Check if the source file exists
if (file_exists($source)) {
    // Attempt to copy the file
    if (copy($source, $destination)) {
        echo "File copied successfully to $destination.";
    } else {
        echo "Failed to copy file.";
    }
} else {
    echo "Source file does not exist.";
}
?>
