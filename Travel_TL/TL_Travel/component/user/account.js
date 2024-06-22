import { useContext } from "react";
import { View, Text } from "react-native";
import { Avatar, Button, Card, Chip, List} from "react-native-paper";
import MyStyle from "../../styles/MyStyle";
import {MyDispatchContext, MyUserContext } from "../../configs/context";
import StyleforLogin from "./StyleforLogin";
import Icon from "react-native-vector-icons/FontAwesome6"
import { useWindowDimensions } from "react-native";



const Account = () => {
    const user = useContext(MyUserContext);
    const dispatch = useContext(MyDispatchContext);
    const { width } = useWindowDimensions();
   
    return (
        <View style={[MyStyle.container, MyStyle.margin]}>
            
            <Avatar.Image style={StyleforLogin.avatar}size={280} source={{uri: `${user.Avatar}`.startsWith("https://tlinh.pythonanywhere.com/static")? `${user.Avatar}`:`https://tlinh.pythonanywhere.com/static${user.Avatar}`}} />
            
           <Button style={StyleforLogin.hello}><Text style={StyleforLogin.textinhello}><Icon size={18} style={StyleforLogin.m_10} name="suitcase-rolling"></Icon>  Xin chào, {user.last_name}</Text></Button>
            <List.Section>
                <Text style={StyleforLogin.text}><Icon name="envelope-open-text" size={19}/>      {user.email}</Text>
                <Text style={StyleforLogin.text}><Icon name="location-dot" size={19}/>{user.address}</Text>
                
                <Text style={StyleforLogin.text}><Icon name="mobile-retro" size={19}/>{user.sdt}</Text>
            </List.Section>
            <Button style={StyleforLogin.bnt} onPress={() => dispatch({"type": "logout"})}><Icon size={18} color="white" name="right-from-bracket" /><Text style={StyleforLogin.out}>  Đăng xuất</Text></Button>
        </View>
    );
}

// https://www.pythonanywhere.com/user/tLinh/files/home/tLinh/LTHD_Travel/Travel_TL/Travel/static/imageForTour/2024/06/Screenshot_2024-05-25_232326.png
// https://www.pythonanywhere.com/user/tLinh/files/home/tLinh/LTHD_Travel/Travel_TL/Travel/static/Travel/2024/06/Screenshot_2024-06-01_220635.png
// https://tlinh.pythonanywhere.com/static/Travel/2024/06/Screenshot_2024-06-01_220635.png
// https://tlinh.pythonanywhere.com/static/imageForTour/2024/06/Screenshot_2024-05-25_233736.p


export default Account;


