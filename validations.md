# Validating

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | Screenshot | Notes |
| --- | --- | --- |
| Home/Index | ![screenshot](static/images/p4-home-html-val.png) | Pass: No Errors |
| Items | ![screenshot](static/images/p4-items-html-val.png) | Pass: No Errors |
| Items Edit Review| ![screenshot](static/images/p4-edit-review-html-val.png) | Pass: No Errors |
| Items Delete Review| ![screenshot](static/images/p4-delete-review-html-val.png) | Pass: No Errors |
| Items Edit Item| ![screenshot](static/images/p4-edit-item-html-val.png) | Pass: No Errors |
| Items Delete Item| ![screenshot](static/images/p4-delete-item-html-val.png) | Pass: No Errors |
| Items Add Item| ![screenshot](static/images/p4-add-item-html-val.png) | Pass: No Errors |
| Trolley | ![screenshot](static/images/p4-trolley-html-val.png) | Pass: No Errors |
| Who We Are | ![screenshot](static/images/who-we-are-html-val.png) | Pass: No Errors |
| Profile | ![screenshot](static/images/p4-profile-html-val.png) | Pass: No Errors |
| Register | ![screenshot](static/images/p4-register-html-val.png) | Pass: No Errors |
| Login | ![screenshot](static/images/p4-login-html-val.png) | Pass: No Errors |
| Item Details | ![screenshot](static/images/p4-item-details-html-val.png) | Pass: No Errors |
| Edit Review | ![screenshot](static/images/p4-edit-review-html-val.png) | Pass: No Errors |
| Delete Review | ![screenshot](static/images/p4-delete-review-html-val.png) | Pass: No Errors |
| Logout | ![screenshot](static/images/p4-logout-html-val.png) | Pass: No Errors |
| Checkout | ![screenshot](static/images/p4-checkout-html-val.png) | Pass: No Errors |
| Checkout Success | ![screenshot](static/images/p4-checkout-success-html-val.png) | Pass: No Errors |
| Email confirm | ![screenshot]() | Pass: No Errors |
| Password Change | ![screenshot](static/images/change-password-html-val.png) | Pass: No Errors |
| Password Reset Done | ![screenshot](static/images/password-reset-done-val%20(2).png) | Pass: No Errors |
| Password Reset From Key Done | ![screenshot]() | Pass: No Errors |
| Password Reset From Key | ![screenshot]() | Pass: No Errors |
| Password Reset | ![screenshot](static/images/forgot-password-val.png) | Pass: No Errors |
| Verification Sent | ![screenshot](static/images/verify-email-val.png) | Pass: No Errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| base.css | ![screenshot](static/images/p4-basecss.val.png) | Pass: No Errors |
| checkout.css | ![screenshot](static/images/p4-checkout-css-val.png) | Pass: No Errors |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![screenshot](static/images/js-hint-stripe-elements.png) | Pass: No Errors |
| save-toggle-script.js | ![screenshot](static/images/js-hint-save-toggle.png) | Pass: No Errors |
| quantity-input.js | ![screenshot](static/images/js-hint-quantity-input.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

#### Validation For Green_Jacket App
| File | Screenshot | Notes |
| --- | --- | --- |
| settings.py | ![screenshot]() | AUTH_PASSWORD_VALIDATORS lines too long (django code) |
| urls.py | ![screenshot]() | Pass: No Errors |

#### Validation For Checkout App
| File | Screenshot | Notes |
| --- | --- | --- |
| init.py | ![screenshot]() | Pass: No Errors |
| admin.py | ![screenshot]() | Pass: No Errors |
| apps.py | ![screenshot]() | Pass: No Errors |
| forms.py | ![screenshot]() | Pass: No Errors |
| models.py | ![screenshot]() | Pass: No Errors |
| signals.py | ![screenshot]() | Pass: No Errors |
| urls.py | ![screenshot]() | Pass: No Errors |
| views.py | ![screenshot]() | Pass: No Errors |
| webhook_handler.py | ![screenshot]() | Pass: No Errors |
| webhooks.py | ![screenshot]() | Pass: No Errors |

#### Validation For Accounts App
| File | Screenshot | Notes |
| --- | --- | --- |
| forms.py | ![screenshot]() | Pass: No Errors |
| urls.py | ![screenshot]() | Pass: No Errors |
| views.py | ![screenshot]() | Pass: No Errors |

#### Validation For Core App
| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot]() | Pass: No Errors |
| apps.py | ![screenshot]() | Pass: No Errors |
| forms.py | ![screenshot]() | Pass: No Errors |
| models.py | ![screenshot]() | Pass: No Errors |
| urls.py | ![screenshot]() | Pass: No Errors |
| views.py | ![screenshot]() | Pass: No Errors |

#### Validation For Items App
| File | Screenshot | Notes |
| --- | --- | --- |
| trolley_tags.py | ![screenshot]() | Pass: No Errors |
| item_tags.py | ![screenshot]() | Pass: No Errors |
| admin.py | ![screenshot]() | Pass: No Errors |
| apps.py | ![screenshot]() | Pass: No Errors |
| context_processors.py | ![screenshot]() | Pass: No Errors |
| forms.py | ![screenshot]() | Pass: No Errors |
| models.py | ![screenshot]() | Pass: No Errors |
| urls.py | ![screenshot]() | Pass: No Errors |
| views.py | ![screenshot]() | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot]() | Works as expected |
| Firefox | ![screenshot]() | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot]() | Works as expected |
| Tablet (DevTools) | ![screenshot]() | Works as expected |
| Desktop | ![screenshot]() | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

### Green_Jacket Templates - Mobile Testing
| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home/Index | mobile | ![screenshot]() |  |
| Items | mobile | ![screenshot]() |  |
| Who We Are | mobile | ![screenshot]() |  |
| Contact | mobile | ![screenshot]() |  |
| Profile | mobile | ![screenshot]() |  |
| Register | mobile | ![screenshot]() |  |
| Login | mobile | ![screenshot]() |  |
| Item Details | mobile | ![screenshot]() |  |
| Edit Review | mobile | ![screenshot]() |  |
| Delete Review | mobile | ![screenshot]() |  |
| Edit Profile | mobile | ![screenshot]() |  |
| Order Details | mobile | ![screenshot]() |  |
| Logout | mobile | ![screenshot]() |  |
| Trolley | mobile | ![screenshot]() |  |
| Checkout | mobile | ![screenshot]() |  |
| Checkout Success | mobile | ![screenshot]() |  |
| Email confirm | mobile | ![screenshot]() |  |
| Verification Sent | mobile | ![screenshot]() |  |
| Verified Email Required | mobile | ![screenshot]() |  |

[Back to Top](#top)