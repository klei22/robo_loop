echo "Listening for the first image on /CoreNode/grey_img..."

# Use rostopic echo to capture the data, process it with awk to extract the image data.
# The awk script stops processing when it sees the second "header" indicating a new message.
rostopic echo /CoreNode/grey_img | awk '
BEGIN {print_data=0}
/header:/ {
    count += 1;
    if (count == 2) {exit}
    if (count == 1) {print_data=1; next}
}
print_data && /^data:/ {
    print $0; # Print the "data" line containing the image data
    print_data=0; # Stop printing after the data field
}
' > image.txt

echo "The image data has been saved to /path/to/your/image.txt"

