    document.addEventListener('DOMContentLoaded', function () {
        // Open review modal
        const modal = document.getElementById('modal');
        const openBtn = document.getElementById('open-review-modal');

        if (openBtn && modal) {
            openBtn.addEventListener('click', function (e) {
                e.preventDefault();  // prevent link navigation if <a>
                modal.style.display = 'flex'; // show modal
            });
        }

        // Save for Later alert if not logged in
        const saveWrapper = document.getElementById('save-click-wrapper');
        const saveButton = document.getElementById('save-button');
        const isAuthenticated = saveButton.dataset.authenticated === "true";

        if (!isAuthenticated && saveWrapper && saveButton) {
            saveWrapper.addEventListener('click', function (e) {
                e.preventDefault();
                Swal.fire({
                    icon: 'info',
                    title: 'Login Required',
                    text: 'Please log in to save this item for later.',
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'OK'
                });
            });
        }
    });
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

    document.addEventListener('DOMContentLoaded', function () {
        const modal = document.getElementById('modal');
        const openBtn = document.getElementById('open-review-modal');

        if (openBtn && modal) {
            openBtn.addEventListener('click', function (e) {
                e.preventDefault();  // prevent link navigation if <a>
                modal.style.display = 'flex'; // show modal
            });
        }
    });