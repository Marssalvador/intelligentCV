import React, { useState } from 'react';
import axios from 'axios';
// Material UI
import { Button, TextField, Typography } from '@mui/material';

export default function UploadCV() {
    const [file, setFile] = useState(null);
    const [title, setTitle] = useState('');

    const handleSubmit = async () => {
        const formData = new FormData();
        formData.append('job_title', title);
        formData.append('cv_file', file);
        const response = await axios.post('/api/upload/', formData);
        console.log('Evaluación recibida:', response.data);
    };

    return (
        <div className="p-4">
            <Typography variant="h5">Cargar CV y Descripción de Puesto</Typography>
            <TextField
                label="Título del Puesto"
                value={title}
                onChange={e => setTitle(e.target.value)}
                fullWidth
                margin="normal"
            />
            <input
                type="file"
                accept=".pdf,.docx,.txt"
                onChange={e => setFile(e.target.files[0])}
            />
            <Button variant="contained" onClick={handleSubmit} className="mt-4">
                Enviar para Evaluación
            </Button>
        </div>
    );
}