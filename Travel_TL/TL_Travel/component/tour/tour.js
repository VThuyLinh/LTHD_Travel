import { StatusBar, StyleSheet, View } from "react-native"
import MyStyle from "../../styles/MyStyle"
import { Text } from "react-native-paper"

const Tour =() =>
    {
        return(
        <View style={MyStyle.container}>
            <Text>Bạn muốn đi đến đâu ???</Text>
        </View>
        );
    }

export default Tour;