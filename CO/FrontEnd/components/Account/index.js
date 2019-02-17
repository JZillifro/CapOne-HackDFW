import React from 'react';
import { Platform, StatusBar, StyleSheet, View, Text } from 'react-native';
import { Button, ThemeProvider, Input, Image, Header } from 'react-native-elements';
import Icon from 'react-native-vector-icons/FontAwesome';
import PageHeader from '../PageHeader';

export default class Account extends React.Component {
  state = {
    username: null,
    password: null
  };

  render() {
    if (!this.props.user) {
      return (
        <View>
          <View style={styles.login}>
            <Image
              source={require('./money.jpg')}
              style={{ width: 200, height: 200 }}
              />
            <Input
              placeholder='username'
              leftIcon={{ type: 'font-awesome', name: 'user' }}
              style={styles.inp}
              onChangeText={(username) => this.setState({username})}
              />
            <Input
              placeholder='password'
              leftIcon={{ type: 'font-awesome', name: 'lock' }}
              style={styles.inp}
              onChangeText={(password) => this.setState({password})}
              />
            <View style={styles.inp}>
              <Button title="Log in" onClick={() => this.props.handleLogin(this.state.username, this.state.password)}/>
            </View>
          </View>
        </View>
      );
    } else {
      return (
        <View>
          <Header>
            <Text>Account</Text>
          </Header>
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
  },
  head: {
    textAlign: 'center'
  }

})
