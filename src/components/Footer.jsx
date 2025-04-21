import React from 'react';

const Footer = () => {
    return (
        <footer>
            <p>&copy; {new Date().getFullYear()} LinkCargo. All rights reserved.</p>
            <nav>
                <a href="/terms">Terms & Conditions</a> | <a href="/faq">FAQ</a> | <a href="/contact">Contact</a>
            </nav>
        </footer>
    );
};

export default Footer;
