document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('videoForm');
    const loading = document.getElementById('loading');
    const result = document.getElementById('result');
    const videoElement = document.getElementById('generatedVideo');
    const videoSource = document.getElementById('videoSource');
    const enhancedPromptDiv = document.getElementById('enhancedPrompt');
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        loading.classList.remove('hidden');
        result.classList.add('hidden');
        
        const formData = new FormData(form);
        
        try {
            const response = await fetch('/generate', {
                method: 'POST',
                body: formData
            });
            
            if (!response.ok) {
                throw new Error('Server error: ' + response.status);
            }
            
            const data = await response.json();
            
            videoSource.src = data.video_url;
            videoElement.load();
            
            enhancedPromptDiv.innerHTML = `<strong>Enhanced Prompt:</strong> ${data.enhanced_prompt}`;
            
            result.classList.remove('hidden');
            loading.classList.add('hidden');
            
            result.scrollIntoView({ behavior: 'smooth' });
            
        } catch (error) {
            console.error('Error:', error);
            alert('Error generating video: ' + error.message);
            loading.classList.add('hidden');
        }
    });
});