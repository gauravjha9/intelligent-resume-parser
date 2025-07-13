const API_BASE_URL = 'http://127.0.0.1:8000/api/v1';

async function uploadResume() {
    const input = document.getElementById('resumeInput');
    const output = document.getElementById('jsonOutput');
    const file = input.files[0];

    if (!file) {
        alert('Please select a resume (PDF or DOCX)');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    output.classList.remove('hidden');
    output.textContent = 'Parsing resume...';

    try {
        const response = await fetch(`${API_BASE_URL}/upload-file`, {
            method: 'POST',
            body: formData
        });



        if (!response.ok) {
            throw new Error('Failed to parse resume.');
        }

        const result = await response.json();
        output.textContent = JSON.stringify(result, null, 2);
    } catch (error) {
        output.textContent = `Error: ${error.message}`;
    }
}