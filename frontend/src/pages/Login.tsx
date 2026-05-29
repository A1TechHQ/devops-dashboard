import React from 'react';
import { Box, TextField, Button, Container, Paper, Typography } from '@mui/material';
import axios from 'axios';

interface LoginProps {
  onLoginSuccess: () => void;
}

const Login: React.FC<LoginProps> = ({ onLoginSuccess }) => {
  const [email, setEmail] = React.useState('admin@example.com');
  const [password, setPassword] = React.useState('admin123');
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState('');

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await axios.post('/api/auth/login', null, {
        params: { email, password }
      });
      
      localStorage.setItem('access_token', response.data.access_token);
      onLoginSuccess();
    } catch (err) {
      setError('Invalid credentials');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="sm">
      <Box sx={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: '100vh'
      }}>
        <Paper sx={{ p: 4, width: '100%' }}>
          <Typography variant="h4" gutterBottom align="center">
            DevOps Dashboard
          </Typography>
          <Typography variant="body2" gutterBottom align="center" sx={{ mb: 3 }}>
            Sign in to your account
          </Typography>

          <form onSubmit={handleLogin}>
            <TextField
              fullWidth
              label="Email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              margin="normal"
              required
            />
            <TextField
              fullWidth
              label="Password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              margin="normal"
              required
            />

            {error && (
              <Typography color="error" sx={{ mt: 2, mb: 2 }}>
                {error}
              </Typography>
            )}

            <Button
              fullWidth
              variant="contained"
              sx={{ mt: 3 }}
              onClick={handleLogin}
              disabled={loading}
            >
              {loading ? 'Signing in...' : 'Sign In'}
            </Button>
          </form>

          <Typography variant="body2" sx={{ mt: 3, textAlign: 'center', color: '#666' }}>
            Demo Credentials:<br />
            Email: admin@example.com<br />
            Password: admin123
          </Typography>
        </Paper>
      </Box>
    </Container>
  );
};

export default Login;
