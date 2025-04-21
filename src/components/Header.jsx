import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';

const Header = () => {
    const [menuOpen, setMenuOpen] = useState(false);

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    };

    return (
        <header>
            <div className="logo">LinkCargo</div>
            <button className="hamburger" onClick={toggleMenu}>
                ☰
            </button>
            <div className={`nav-container ${menuOpen ? 'open' : ''}`}>
                <nav className="left-nav">
                    <NavLink to="/" onClick={() => setMenuOpen(false)}>Home</NavLink>
                    <NavLink to="/post-trip" onClick={() => setMenuOpen(false)}>Post Trip</NavLink>
                    <NavLink to="/post-package" onClick={() => setMenuOpen(false)}>Post Package</NavLink>
                </nav>
                <nav className="right-nav">
                    <NavLink to="/profile" onClick={() => setMenuOpen(false)}>Profile</NavLink>
                    <NavLink to="/login" onClick={() => setMenuOpen(false)}>Login</NavLink>
                </nav>
            </div>
        </header>
    );
};

export default Header;
