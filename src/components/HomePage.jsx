import React from 'react';

const HomePage = () => {
    return (
        <div className="home-page">
            <h1>Welcome to LinkCargo</h1>
            <p>
                Please ensure all listings comply with our terms: no illegal or prohibited items. 
                All users must verify their identity before posting.
            </p>
            <button className="view-packages">View Packages</button>
            <footer>
                © 2025 LinkCargo. All rights reserved.
                <br />
                <a href="/terms">Terms & Conditions</a> | <a href="/faq">FAQ</a> | <a href="/contact">Contact</a>
            </footer>
        </div>
    );
};

export default HomePage;