import os

# Define the project file structure and file contents in a dictionary:
project_files = {
    # Public folder
    "public/index.html": r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>LinkCargo</title>
</head>
<body>
    <div id="root"></div>
    <script src="../src/index.js"></script>
</body>
</html>
""",
    # src/assets folder (empty folder, you can add assets later)
    # src/components
    "src/components/Header.jsx": r"""import React from 'react';
import { NavLink } from 'react-router-dom';

const Header = () => {
    return (
        <header>
            <div className="logo">LinkCargo</div>
            <nav>
                <NavLink to="/">Home</NavLink>
                <NavLink to="/post-trip">Post Trip</NavLink>
                <NavLink to="/post-package">Post Package</NavLink>
                <NavLink to="/profile">Profile</NavLink>
                <NavLink to="/login">Login</NavLink>
            </nav>
        </header>
    );
};

export default Header;
""",
    "src/components/Footer.jsx": r"""import React from 'react';

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
""",
    "src/components/TripCard.jsx": r"""import React from 'react';
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
""",
    "src/components/PackageCard.jsx": r"""import React from 'react';
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
""",
    "src/components/SafetyInfo.jsx": r"""import React from 'react';

const SafetyInfo = () => {
    return (
        <div className="safety-info">
            <p>Please ensure all listings comply with our terms: no illegal or prohibited items. 
            All users must verify their identity before posting.</p>
        </div>
    );
};

export default SafetyInfo;
""",
    # src/pages
    "src/pages/HomePage.jsx": r"""import React, { useState, useEffect } from 'react';
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
""",
    "src/pages/TripPostingPage.jsx": r"""import React, { useState } from 'react';

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
                <input type="text" name="fromCity" placeholder="From City" onChange={handleChange} required />
                <input type="text" name="toCity" placeholder="To City" onChange={handleChange} required />
                <input type="date" name="departureDate" onChange={handleChange} required />
                <input type="number" name="availableWeight" placeholder="Available Weight (kg)" onChange={handleChange} required />
                <input type="number" name="pricePerKg" placeholder="Price per kg" onChange={handleChange} required />
                <label>
                    <input type="checkbox" name="confirmation" onChange={handleChange} required />
                    I confirm that no illegal or prohibited items are included.
                </label>
                <button type="submit">Post Trip</button>
            </form>
        </div>
    );
};

export default TripPostingPage;
""",
    "src/pages/PackagePostingPage.jsx": r"""import React, { useState } from 'react';

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
""",
    "src/pages/ListingDetailPage.jsx": r"""import React from 'react';

const ListingDetailPage = ({ match }) => {
    // Use match.params.id to fetch listing details from Firebase Firestore
    return (
        <div className="listing-detail-page">
            <h1>Listing Details</h1>
            <p>Details for listing with ID: {match.params.id}</p>
            {/* Details and in-app chat can be added here */}
        </div>
    );
};

export default ListingDetailPage;
""",
    "src/pages/ProfilePage.jsx": r"""import React from 'react';

const ProfilePage = () => {
    // Fetch user details and listing history
    return (
        <div className="profile-page">
            <h1>Your Profile</h1>
            <p>User details and listing history will be displayed here.</p>
        </div>
    );
};

export default ProfilePage;
""",
    "src/pages/ChatPage.jsx": r"""import React from 'react';

const ChatPage = () => {
    // Chat functionality will be implemented later
    return (
        <div className="chat-page">
            <h1>Chat</h1>
            <p>Messaging functionality coming soon.</p>
        </div>
    );
};

export default ChatPage;
""",
    # Firebase files
    "src/firebase/firebaseConfig.js": r"""import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/firestore';
import 'firebase/storage';

const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

firebase.initializeApp(firebaseConfig);

const auth = firebase.auth();
const firestore = firebase.firestore();
const storage = firebase.storage();

export { auth, firestore, storage };
""",
    "src/firebase/firebaseService.js": r"""import { firestore, storage } from './firebaseConfig';

// Function to create a new document in a specified collection
export const createDocument = async (collection, data) => {
    try {
        const docRef = await firestore.collection(collection).add(data);
        return docRef.id;
    } catch (error) {
        console.error('Error adding document: ', error);
        throw error;
    }
};

// Function to upload file to Firebase Storage
export const uploadFile = async (path, file) => {
    try {
        const storageRef = storage.ref();
        const fileRef = storageRef.child(path);
        await fileRef.put(file);
        return await fileRef.getDownloadURL();
    } catch (error) {
        console.error('Error uploading file: ', error);
        throw error;
    }
};
""",
    # App.jsx, index.js and optional routes
    "src/App.jsx": r"""import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import TripPostingPage from './pages/TripPostingPage';
import PackagePostingPage from './pages/PackagePostingPage';
import ListingDetailPage from './pages/ListingDetailPage';
import ProfilePage from './pages/ProfilePage';
import ChatPage from './pages/ChatPage';

const App = () => {
    return (
        <Router>
            <Header />
            <Switch>
                <Route exact path="/" component={HomePage} />
                <Route path="/post-trip" component={TripPostingPage} />
                <Route path="/post-package" component={PackagePostingPage} />
                <Route path="/listing/:id" component={ListingDetailPage} />
                <Route path="/profile" component={ProfilePage} />
                <Route path="/chat" component={ChatPage} />
            </Switch>
            <Footer />
        </Router>
    );
};

export default App;
""",
    "src/index.js": r"""import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles/main.css';

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
);
""",
    "src/routes.js": r"""/**
 * Optional file to manage routes.
 * This file can be used if you want to centralize route definitions.
 */

export const routes = {
    home: '/',
    postTrip: '/post-trip',
    postPackage: '/post-package',
    listing: '/listing',
    profile: '/profile',
    chat: '/chat'
};
""",
    "src/styles/main.css": r"""body {
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}

header, footer {
    background-color: #333;
    color: #fff;
    padding: 1rem;
}

nav a {
    margin: 0 1rem;
    color: #fff;
    text-decoration: none;
}

.trip-card, .package-card {
    border: 1px solid #ccc;
    padding: 1rem;
    margin: 1rem 0;
}

.home-page {
    padding: 1rem;
}
""",
    # Root files
    ".gitignore": r"""node_modules/
build/
.firebase/
.env
""",
    "package.json": r"""{
  "name": "linkcargo",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "firebase": "^8.10.0",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-router-dom": "^5.2.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  }
}
""",
    "README.md": r"""# LinkCargo

LinkCargo is a peer-to-peer package delivery platform connecting travelers between Thailand, South Africa, and Zimbabwe.

## Features

- Post trips and package requests
- In-app messaging (coming soon)
- Firebase authentication and Firestore integration
- Safety and legal compliance with user verification

## Getting Started

1. Clone the repository
2. Run `npm install`
3. Setup Firebase configuration in `src/firebase/firebaseConfig.js`
4. Run `npm start` to launch the development server

## Future Enhancements

- Mobile app development using React Native
- Escrow service integration
- Enhanced chat and notification system
"""
}

def create_project_structure(project_files):
    for filepath, content in project_files.items():
        # Get directory of file
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        # Write file content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created file: {filepath}")

if __name__ == '__main__':
    create_project_structure(project_files)
    print("LinkCargo project structure created successfully!")
