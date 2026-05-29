import React from 'react';
import { Box, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import axios from 'axios';

const Servers: React.FC = () => {
  const [servers, setServers] = React.useState<any[]>([]);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    const fetchServers = async () => {
      try {
        const token = localStorage.getItem('access_token');
        const response = await axios.get('/api/servers', {
          headers: { Authorization: `Bearer ${token}` }
        });
        setServers(response.data);
      } catch (error) {
        console.error('Failed to fetch servers:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchServers();
  }, []);

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Servers
      </Typography>

      {loading ? (
        <Typography>Loading servers...</Typography>
      ) : (
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow sx={{ backgroundColor: '#f5f5f5' }}>
                <TableCell>Name</TableCell>
                <TableCell>Hostname</TableCell>
                <TableCell>IP Address</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Last Heartbeat</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {servers.map((server) => (
                <TableRow key={server.id}>
                  <TableCell>{server.name}</TableCell>
                  <TableCell>{server.hostname}</TableCell>
                  <TableCell>{server.ip_address}</TableCell>
                  <TableCell>
                    <Box sx={{
                      display: 'inline-block',
                      padding: '4px 12px',
                      borderRadius: '4px',
                      backgroundColor: server.status === 'online' ? '#4caf50' : '#f44336',
                      color: 'white',
                      fontSize: '12px'
                    }}>
                      {server.status}
                    </Box>
                  </TableCell>
                  <TableCell>{new Date(server.last_heartbeat).toLocaleString()}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Box>
  );
};

export default Servers;
