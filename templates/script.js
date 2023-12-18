document.addEventListener("DOMContentLoaded", function () {
    const talukaDropdown = document.getElementById("talukaDropdown");
    const imageContainer = document.getElementById("imageContainer");

    // Define an object to map taluka names to image URLs
    const talukaImageMap = {
        taluka1: "C:\Users\srikanth\Desktop\sales_updated\templates\asset\simn6065.png",
        taluka2: "path/to/taluka2.jpg",
        taluka3: "path/to/taluka3.jpg",
        taluka2: "path/to/taluka2.jpg",
        taluka3: "path/to/taluka3.jpg",
        taluka2: "path/to/taluka2.jpg",
        taluka3: "path/to/taluka3.jpg",
        taluka2: "path/to/taluka2.jpg",
        taluka3: "path/to/taluka3.jpg",
        // Add more talukas and image paths as needed
    };

    talukaDropdown.addEventListener("change", function () {
        const selectedTaluka = talukaDropdown.value;
        const imageUrl = talukaImageMap[selectedTaluka];

        if (imageUrl) {
            imageContainer.innerHTML = `<img src="${imageUrl}" alt="${selectedTaluka} Image">`;
        } else {
            imageContainer.innerHTML = "<p>No image available for selected taluka.</p>";
        }
    });
});
