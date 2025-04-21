import React, { useState } from 'react';

const PackagePostingPage = () => {
    const [form, setForm] = useState({
        description: '',
        weight: '',
        fromCountry: '',
        toCountry: '',
        offerPrice: '',
        deadline: '',
        confirmation: false
    });

    const handleSubmit = (e) => {
        e.preventDefault();
        // Validate and send package post to Firebase Firestore
        console.log('Posting package:', form);
    };

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setForm({ ...form, [name]: type === 'checkbox' ? checked : value });
    };

    return (
        <div className="package-posting-page">
            <h1>Post a Package</h1>
            <form onSubmit={handleSubmit}>
                <input type="text" name="description" placeholder="Description" onChange={handleChange} required />
                <input type="number" name="weight" placeholder="Weight (kg)" onChange={handleChange} required />
                <input type="text" name="fromCountry" placeholder="From Country" onChange={handleChange} required />
                <input type="text" name="toCountry" placeholder="To Country" onChange={handleChange} required />
                <input type="number" name="offerPrice" placeholder="Offer Price" onChange={handleChange} required />
                <input type="date" name="deadline" onChange={handleChange} required />
                <label>
                    <input type="checkbox" name="confirmation" onChange={handleChange} required />
                    I confirm that no illegal or prohibited items are included.
                </label>
                <button type="submit">Post Package</button>
            </form>
        </div>
    );
};

export default PackagePostingPage;
