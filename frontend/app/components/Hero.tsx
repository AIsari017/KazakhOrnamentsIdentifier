import React from 'react';

const Hero: React.FC = () => {
    return (
        <div className="min-h-screen flex flex-col justify-center items-center bg-gray-50 p-6">
            <h1 className="text-4xl md:text-6xl font-bold text-gray-800 text-center">
                Thank you for exploring my project.
            </h1>
            <p className="mt-4 text-xl text-gray-600 text-center">
                This page is in development.
            </p>
            <a 
                href="https://github.com/AIsari017/KazakhOrnamentsIdentifier" 
                target="_blank" 
                rel="noopener noreferrer" 
                className="mt-6 px-6 py-3 bg-blue-600 text-white rounded-md shadow hover:bg-blue-700 transition duration-300"
            >
                More info on GitHub
            </a>
        </div>
    );
};

export default Hero;