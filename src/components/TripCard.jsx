import React from 'react';
import { Link } from 'react-router-dom';

const TripCard = ({ trip }) => {
    return (
        <div className="trip-card">
            <h3>{trip.fromCity} to {trip.toCity}</h3>
            <p>Date: {trip.departureDate}</p>
            <p>Available Weight: {trip.availableWeight} kg</p>
            <p>Fee: ${trip.pricePerKg} per kg</p>
            <Link to={`/trip/${trip.id}`}>View Details</Link>
        </div>
    );
};

export default TripCard;
