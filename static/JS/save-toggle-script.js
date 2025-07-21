document.addEventListener('DOMContentLoaded', function () {
    // --- Review Modal ---
    const modal = document.getElementById('modal');
    const openBtn = document.getElementById('open-review-modal');
    if (openBtn && modal) {
        openBtn.addEventListener('click', function (e) {
            e.preventDefault();
            modal.style.display = 'flex';  // Show the modal (flex container)
        });
    }

    // --- Save for Later Alert if User Not Logged In ---
    const saveWrapper = document.getElementById('save-click-wrapper');
    const saveButton = document.getElementById('save-button');
    if (saveButton) {
        const isAuthenticated = saveButton.dataset.authenticated === "true";
        if (!isAuthenticated && saveWrapper) {
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
    }

    // --- Save for Later Form Submission via AJAX ---
    const form = document.getElementById('save-form');
    if (form) {
        const heartIcon = document.getElementById('heart-icon');
        const saveText = document.getElementById('save-text');

        form.addEventListener('submit', function (e) {
            e.preventDefault();

            const formData = new FormData(form);
            const action = form.getAttribute('action');

            fetch(action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.saved) {
                    // Change heart icon to solid and update text
                    heartIcon.classList.replace('far', 'fas');
                    saveText.textContent = 'Saved';
                } else {
                    // Change heart icon to outline and update text
                    heartIcon.classList.replace('fas', 'far');
                    saveText.textContent = 'Save for Later';
                }
            })
            .catch(error => {
                console.error('Error submitting form:', error);
            });
        });
    }

    // --- Scroll to Top and Sort Handling (jQuery-dependent) ---
    if (typeof $ !== 'undefined') {
        // Scroll to top on clicking "Back to Top" link
        $('.btt-link').click(function (e) {
            window.scrollTo(0, 0);
        });

        // Sorting select change event: updates URL parameters
        $('#sort-selector').change(function () {
            const selected = $(this).val();
            const currentUrl = new URL(window.location);

            if (selected === 'reset') {
                // Remove sort parameters to reset sorting
                currentUrl.searchParams.delete('sort');
                currentUrl.searchParams.delete('direction');
            } else {
                // Extract sort and direction from value and update URL
                const [sort, direction] = selected.split('_');
                currentUrl.searchParams.set('sort', sort);
                currentUrl.searchParams.set('direction', direction);
            }

            // Redirect to updated URL
            window.location = currentUrl.toString();
        });

        // --- New Item Image Preview Handling ---
        $('#new-image').change(function () {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();

                reader.onload = function (e) {
                    $('#new-image-preview').attr('src', e.target.result);  // Set preview image src
                    $('#preview-container').show();  // Show preview container
                };

                reader.readAsDataURL(file);

                // Show filename under input
                $('#filename').text(`Image will be set to: ${file.name}`);
            } else {
                // Hide preview and clear filename if no file selected
                $('#preview-container').hide();
                $('#filename').text('');
            }
        });
    } else {
        console.warn('jQuery is not loaded. Sort and scroll features will not work.');
    }
});
