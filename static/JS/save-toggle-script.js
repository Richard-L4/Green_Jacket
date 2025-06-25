document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('save-form');
    if (!form) return;

    const heartIcon = document.getElementById('heart-icon');
    const saveText = document.getElementById('save-text');

    form.addEventListener('submit', function (e) {
        e.preventDefault();  // Prevent full page reload

        const formData = new FormData(form);
        const action = form.getAttribute('action');

        fetch(action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => {
            if (!response.ok) throw new Error('Network error');
            return response.json();
        })
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
        .catch(error => {
            console.error('Error submitting form:', error);
        });
    });
});

