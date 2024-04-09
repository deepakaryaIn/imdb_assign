$(document).ready(function() {
    // Function to fetch upload progress from the server
    function getUploadProgress() {
        $.ajax({
            url: '/progress',  // Endpoint to fetch upload progress
            method: 'GET',
            success: function(response) {
                // Update the progress text
                $('#progress').text('Upload Progress: ' + response.progress + '%');
            },
            error: function(xhr, status, error) {
                console.error('Error fetching upload progress:', error);
            }
        });
    }

    // Periodically fetch upload progress every 5 seconds (adjust as needed)
    setInterval(getUploadProgress, 5000);  // Fetch progress every 5 seconds
});
