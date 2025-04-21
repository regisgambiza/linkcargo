import React from 'react';
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
