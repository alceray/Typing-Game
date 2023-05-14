import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import { Grid, Button, ButtonGroup, Typography } from "@mui/material";

function Home() {
  return (
    <Router>
      <Routes>
        <Route
          exact
          path="/"
          element={
            <Grid container spacing={3}>
              <Grid item xs={12} align="center">
                <Typography variant="h2">Typing Game</Typography>
              </Grid>
              <Grid item xs={12} align="center">
                <Button
                  color="primary"
                  variant="contained"
                  component={Link}
                  to="/type"
                >
                  Start Typing
                </Button>
              </Grid>
            </Grid>
          }
        />
      </Routes>
    </Router>
  );
}

export default Home;
