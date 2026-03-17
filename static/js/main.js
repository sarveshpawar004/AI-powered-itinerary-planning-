// Main JS - Interactions & Route Handling

// Visual Selector Function
function selectOption(element, inputId) {
    // 1. Remove 'selected' class from siblings
    const parent = element.parentElement;
    const siblings = parent.getElementsByClassName('option-card');
    for (let sib of siblings) {
        sib.classList.remove('selected');
    }

    // 2. Add 'selected' to clicked element
    element.classList.add('selected');

    // 3. Update hidden input value
    const val = element.getAttribute('data-value');
    document.getElementById(inputId).value = val;
}

const tripForm = document.getElementById('tripForm');

if (tripForm) {
    tripForm.addEventListener('submit', async function (e) {
        e.preventDefault();

        // UI Loading State
        const btn = tripForm.querySelector('button[type="submit"]');
        const btnText = document.getElementById('btnText');
        const btnLoader = document.getElementById('btnLoader');

        btn.disabled = true;
        btnText.style.display = 'none';
        btnLoader.style.display = 'inline-block';

        // Collect Data
        const data = {
            destination: document.getElementById('destination').value,
            start_date: document.getElementById('start_date').value,
            duration: document.getElementById('duration').value,
            budget: document.getElementById('budget').value,
            style: document.getElementById('style').value, // Now gets value from hidden input
            transport: document.getElementById('transport').value // Now gets value from hidden input
        };

        try {
            const response = await fetch('/generate_trip', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'API Error');
            }

            const result = await response.json();

            // Redirect to the new dedicated result page
            if (result.success) {
                window.location.href = `/result`;
            }

        } catch (error) {
            console.error('Error:', error);
            alert(`Something went wrong: ${error.message}`);
            // In a real app we might handle partial errors better
        } finally {
            // Reset UI (though redirect usually happens first)
            btn.disabled = false;
            btnText.style.display = 'inline-block';
            btnLoader.style.display = 'none';
        }
    });
}
