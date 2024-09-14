function showForm(projectId, commentId) {
    var commentForm = document.getElementById('comment-form-' + projectId + '-' + commentId);
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


function showChildren(parentClass, kidsRoom) {
    var children = document.querySelectorAll('.' + parentClass);

    var kidsRoom = document.getElementById(kidsRoom);
    
    children.forEach(function(child) {
        kidsRoom.appendChild(child);

        child.removeAttribute('hidden');
        child.style.paddingLeft = '80px';
    });
}