import React from 'react'
import UploadCV from './components/UploadCV'

export default function App() {
    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Intelligent CV Review</h1>
            <UploadCV />
        </div>
    )
}