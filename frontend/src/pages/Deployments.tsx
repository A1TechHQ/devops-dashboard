import React from 'react';
import { Box, Typography } from '@mui/material';

const Deployments: React.FC = () => {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Deployments
      </Typography>
      <Typography>Deployment history and status tracking</Typography>
    </Box>
  );
};

export default Deployments;
