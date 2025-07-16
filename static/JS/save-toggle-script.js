document.addEventListener('DOMContentLoaded', function () {
    // Review modal
    const modal = document.getElementById('modal');
    const openBtn = document.getElementById('open-review-modal');
    if (openBtn && modal) {
        openBtn.addEventListener('click', function (e) {
            e.preventDefault();
            modal.style.display = 'flex';
        });
    }

    // Save for Later alert if not logged in
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

    // Save for Later form
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
                    heartIcon.classList.replace('far', 'fas');
                    saveText.textContent = 'Saved';
                } else {
                    heartIcon.classList.replace('fas', 'far');
                    saveText.textContent = 'Save for Later';
                }
            })
            .catch(error => {
                console.error('Error submitting form:', error);
            });
        });
    }

    // Scroll to top and sort handling (jQuery section)
    if (typeof $ !== 'undefined') {
        $('.btt-link').click(function (e) {
            window.scrollTo(0, 0);
        });

        $('#sort-selector').change(function () {
            const selected = $(this).val();
            const currentUrl = new URL(window.location);

            if (selected === 'reset') {
                currentUrl.searchParams.delete('sort');
                currentUrl.searchParams.delete('direction');
            } else {
                const [sort, direction] = selected.split('_');
                currentUrl.searchParams.set('sort', sort);
                currentUrl.searchParams.set('direction', direction);
            }

            window.location = currentUrl.toString();
        });
    } else {
        console.warn('jQuery is not loaded. Sort and scroll features will not work.');
    }
});

  $('#new-image').change(function() {
            var file = this.files[0];
            if (file) {
                var reader = new FileReader();
                reader.onload = function(e) {
                    $('#new-image-preview').attr('src', e.target.result);
                    $('#preview-container').show();
                }
                reader.readAsDataURL(file);
                $('#filename').text(`Image will be set to: ${file.name}`);
            } else {
                $('#preview-container').hide();
                $('#filename').text('');
            }
        });

