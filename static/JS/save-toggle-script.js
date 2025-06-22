document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('save-form');
    if (!form) return;

    const button = document.getElementById('save-button');
    const heartIcon = document.getElementById('heart-icon');
    const saveText = document.getElementById('save-text');

    const url = form.dataset.url;
    const csrfToken = form.dataset.csrf;

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        })
        .then(response => response.json())
        .then(data => {
            if (data.saved) {
                heartIcon.classList.remove('far');
                heartIcon.classList.add('fas');
                saveText.textContent = 'Saved';
            } else {
                heartIcon.classList.remove('fas');
                heartIcon.classList.add('far');
                saveText.textContent = 'Save for Later';
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
