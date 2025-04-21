import React, { useState } from 'react';

const TripPostingPage = () => {
    const [form, setForm] = useState({
        fromCity: '',
        toCity: '',
        departureDate: '',
        availableWeight: '',
        pricePerKg: '',
        confirmation: false
    });

    const handleSubmit = (e) => {
        e.preventDefault();
        // Validate and send trip post to Firebase Firestore
        console.log('Posting trip:', form);
    };

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setForm({ ...form, [name]: type === 'checkbox' ? checked : value });
    };

    return (
        <div className="trip-posting-page">
            <h1>Post a Trip</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    From Country:
                    <select name="fromCity" value={form.fromCity} onChange={handleChange} required>
                        <option value="">Select a country</option>
                        <option value="Zimbabwe">Zimbabwe</option>
                        <option value="Thailand">Thailand</option>
                        <option value="South Africa">South Africa</option>
                    </select>
                </label>
                <label>
                    To Country:
                    <select name="toCity" value={form.toCity} onChange={handleChange} required>
                        <option value="">Select a country</option>
                        <option value="Zimbabwe">Zimbabwe</option>
                        <option value="Thailand">Thailand</option>
                        <option value="South Africa">South Africa</option>
                    </select>
                </label>
                <label>
                    Departure Date:
                    <input type="date" name="departureDate" value={form.departureDate} onChange={handleChange} required />
                </label>
                <label>
                    Available Weight (kg):
                    <input
                        type="number"
                        name="availableWeight"
                        placeholder="Available Weight (kg)"
                        value={form.availableWeight}
                        onChange={handleChange}
                        required
                    />
                </label>
                <label>
                    Price per kg:
                    <input
                        type="number"
                        name="pricePerKg"
                        placeholder="Price per kg"
                        value={form.pricePerKg}
                        onChange={handleChange}
                        required
                    />
                </label>
                <label>
                    <input
                        type="checkbox"
                        name="confirmation"
                        checked={form.confirmation}
                        onChange={handleChange}
                        required
                    />
                    I confirm that no illegal or prohibited items are included.
                </label>
                <button type="submit">Post Trip</button>
            </form>
        </div>
    );
};

export default TripPostingPage;
