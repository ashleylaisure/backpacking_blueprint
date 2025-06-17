
document.addEventListener('DOMContentLoaded', () => {

    const startInput = document.getElementById('start-date'); // Select the start date input by ID
    const endInput = document.getElementById('end-date'); // Select the end date input by ID

    // if editing the form get the value
    const startValue = document.getElementById('start-date').value;
    const endValue = document.getElementById('end-date').value; 

    // use today's date or if editing the current value
    const startDate = startValue ? new Date(startValue) : new Date();
    const endDate = endValue ? new Date(endValue) : new Date();

    // Create a date picker instance
    const startPicker = MCDatepicker.create({
        el: '#start-date',
        dateFormat: 'yyyy-mm-dd', // Set the desired date format
        // closeOnBlur: true, // Close picker when clicking outside
        autoClose: true,
        selectedDate: startDate 
    });

    const endPicker = MCDatepicker.create({
        el: '#end-date',
        dateFormat: 'yyyy-mm-dd', // Set the desired date format
        // closeOnBlur: true, // Close picker when clicking outside
        autoClose: true,
        selectedDate: endDate
    });


    // Open the date picker when the input is clicked
    // startInput.addEventListener("click", () => {startPicker.open();});
    // endInput.addEventListener("click", () => {endPicker.open();});

});