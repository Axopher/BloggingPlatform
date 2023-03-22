document.addEventListener('DOMContentLoaded', function() {
    const alertCloseButtons = document.querySelectorAll('.alert__close');
    
    alertCloseButtons.forEach(function(button) {
      button.addEventListener('click', function(event) {
        event.target.parentNode.parentNode.remove();
      });
    });
  });