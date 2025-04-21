import React, { useState, useEffect } from 'react';
import TripCard from '../components/TripCard';
import PackageCard from '../components/PackageCard';
import SafetyInfo from '../components/SafetyInfo';

const HomePage = () => {
    const [view, setView] = useState('trips');
    const [listings, setListings] = useState([]);

    useEffect(() => {
        // Fetch listings from Firebase Firestore (mock data for now)
        // Example: setListings(data);
    }, [view]);

    return (
        <div className="home-page">
            <h1>Welcome to LinkCargo</h1>
            <div className="search-section">
                {/* Search form to be implemented */}
            </div>
            <div className="listings-section">
                {view === 'trips' ? (
                    listings.map(trip => <TripCard key={trip.id} trip={trip} />)
                ) : (
                    listings.map(pkg => <PackageCard key={pkg.id} pkg={pkg} />)
                )}
            </div>
            <SafetyInfo />
            <button onClick={() => setView(view === 'trips' ? 'packages' : 'trips')}>
                {view === 'trips' ? 'View Packages' : 'View Trips'}
            </button>
        </div>
    );
};

export default HomePage;
