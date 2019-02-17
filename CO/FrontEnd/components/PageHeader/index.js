import React from 'react';
import { Platform, StatusBar, StyleSheet, View, Text } from 'react-native';
import { Button, ThemeProvider, Input, Image, Header } from 'react-native-elements';
import Icon from 'react-native-vector-icons/FontAwesome';

export default class PageHeader extends React.Component {
  state = {
    data: null
  };

  render() {
      return (
        <View>
          <Header style={styles.head} backgroundImage={require('./money.jpg')}>
            <Text>{this.props.title}</Text>
          </Header>
        </View>
      );
  }
}
const styles = StyleSheet.create({
  head: {
    textAlign: 'center'
  }

})
