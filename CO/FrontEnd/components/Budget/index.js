import React from 'react';
import { Platform, StatusBar, StyleSheet, View, Text } from 'react-native';
import { Button, ThemeProvider, Input, Image } from 'react-native-elements';
import Icon from 'react-native-vector-icons/FontAwesome';

export default class Budget extends React.Component {
  state = {
    data: null
  };

  render() {
    if (!this.props.user) {
      return (
        <View style={styles.login}>
            <Text>You're not logged in! Please go log in on the account tab so we can calculate your budget!</Text>
        </View>
      );
    } else {
      return (
        <View>
          <Text>
          {
            this.props.user
          }
          </Text>
        </View>
      );
    }
  }

}
const styles = StyleSheet.create({
  login: {
    alignItems: 'center',
    flex: 1,
    marginTop: '50%'
  },
  inp: {
    marginTop: '5%'
  }

})
