import React from 'react';
import { Link } from 'react-router-dom';

const PackageCard = ({ pkg }) => {
    return (
        <div className="package-card">
            <h3>{pkg.description}</h3>
            <p>Weight: {pkg.weight} kg</p>
            <p>Offer: ${pkg.offerPrice}</p>
            <Link to={`/package/${pkg.id}`}>View Details</Link>
        </div>
    );
};

export default PackageCard;
