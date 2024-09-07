function showForm(projectId) {
    var commentForm = document.getElementById('comment-form-' + projectId);
    if (commentForm) {
        commentForm.removeAttribute('hidden');
    }
}

function cancelForm() {
    var allforms = document.querySelectorAll('.comment-form');
    allforms.forEach(function(form) {
        form.setAttribute('hidden', true);
    });
};
