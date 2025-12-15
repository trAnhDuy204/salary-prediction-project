// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('Salary Predictor App Initialized');
    
    // Add smooth scrolling
    initSmoothScroll();
    
    // Add form validation
    initFormValidation();
    
    // Add animations
    initAnimations();
    
    // Initialize tooltips if Bootstrap is available
    if (typeof bootstrap !== 'undefined') {
        initTooltips();
    }
});

// Smooth Scrolling
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && document.querySelector(href)) {
                e.preventDefault();
                document.querySelector(href).scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Form Validation
function initFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
}

// Animations
function initAnimations() {
    // Fade in elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe all cards and sections
    document.querySelectorAll('.card, .hero-section, .stat-card').forEach(el => {
        observer.observe(el);
    });
}

// Initialize Bootstrap Tooltips
function initTooltips() {
    const tooltipTriggerList = [].slice.call(
        document.querySelectorAll('[data-bs-toggle="tooltip"]')
    );
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// Format number as currency
function formatCurrency(number) {
    return new Intl.NumberFormat('vi-VN', {
        style: 'currency',
        currency: 'VND'
    }).format(number);
}

// Show loading spinner
function showLoading(buttonElement) {
    if (buttonElement) {
        buttonElement.disabled = true;
        const originalText = buttonElement.innerHTML;
        buttonElement.setAttribute('data-original-text', originalText);
        buttonElement.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Đang xử lý...';
    }
}

// Hide loading spinner
function hideLoading(buttonElement) {
    if (buttonElement) {
        buttonElement.disabled = false;
        const originalText = buttonElement.getAttribute('data-original-text');
        if (originalText) {
            buttonElement.innerHTML = originalText;
        }
    }
}

// API Call Helper
async function predictSalary(formData) {
    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

// Display error message
function showError(message, container) {
    const alertHtml = `
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
            <i class="fas fa-exclamation-circle"></i> ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    
    if (container) {
        container.innerHTML = alertHtml;
    } else {
        console.error(message);
    }
}

// Display success message
function showSuccess(message, container) {
    const alertHtml = `
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            <i class="fas fa-check-circle"></i> ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    
    if (container) {
        container.innerHTML = alertHtml;
    } else {
        console.log(message);
    }
}

// Auto-dismiss alerts after 5 seconds
document.querySelectorAll('.alert-dismissible').forEach(alert => {
    setTimeout(() => {
        const bsAlert = new bootstrap.Alert(alert);
        bsAlert.close();
    }, 5000);
});

// Handle form submission with AJAX (if needed)
function handleFormSubmit(formId, onSuccess, onError) {
    const form = document.getElementById(formId);
    if (!form) return;
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const submitBtn = form.querySelector('button[type="submit"]');
        showLoading(submitBtn);
        
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        
        try {
            const result = await predictSalary(data);
            hideLoading(submitBtn);
            
            if (result.success) {
                if (onSuccess) onSuccess(result.data);
            } else {
                if (onError) onError(result.error);
            }
        } catch (error) {
            hideLoading(submitBtn);
            if (onError) onError(error.message);
        }
    });
}

// Utility: Debounce function
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Export functions for use in other scripts
window.salaryPredictorUtils = {
    formatCurrency,
    showLoading,
    hideLoading,
    predictSalary,
    showError,
    showSuccess,
    handleFormSubmit,
    debounce
};

// Console message
console.log('%c Salary Predictor System', 'color: #667eea; font-size: 20px; font-weight: bold;');
console.log('%cDeveloped with ❤️ using Flask & Machine Learning', 'color: #764ba2; font-size: 12px;');