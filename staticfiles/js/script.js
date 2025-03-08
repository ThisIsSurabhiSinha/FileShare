document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    let fileInput = document.getElementById('fileInput');
    if (fileInput.files.length === 0) {
        alert("Please select a file to upload.");
        return;
    }

    let formData = new FormData();
    formData.append('file', fileInput.files[0]);
    console.log(formData)

    try {
        let response = await fetch('http://127.0.0.1:8000/handle/', {
            method: 'POST',
            body: formData
        });
        console.log("print result: ")
        let result = await response.json();
        console.log(result)

        if (response.ok) {
            let shareLinkContainer = document.getElementById('shareLinkContainer');
            let shareLinkInput = document.getElementById('shareLink');
            shareLinkInput.value = result.data.shareable_url;
            shareLinkContainer.classList.remove('hidden');
        } else {
            alert("Error uploading file: " + result.message);
        }
    } catch (error) {
        console.error("Error:", error);
        alert("Something went wrong. Please try again.");
    }
});

function copyLink() {
    let shareLinkInput = document.getElementById('shareLink');
    shareLinkInput.select();
    document.execCommand('copy');
    alert("Link copied to clipboard!");
}
