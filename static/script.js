// Set progress bars
document.querySelectorAll('.card').forEach(card => {
  const progress = card.getAttribute('data-progress') || 0;
  const progressBar = card.querySelector('.progress-bar');
  progressBar.style.width = `${progress}%`;
});

// Show file name on upload
document.querySelectorAll('.file-input').forEach(input => {
  input.addEventListener('change', function () {
    const fileNameDiv = this.closest('.upload-section').querySelector('.file-name');
    if (this.files.length > 0) {
      fileNameDiv.textContent = this.files[0].name;
    } else {
      fileNameDiv.textContent = 'No file uploaded';
    }
  });
});