import React, { useContext, useReducer } from 'react';
import Tour from './component/tour/tour';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import TourDetail from './component/tour/tourdetail';
import { NavigationContainer } from '@react-navigation/native';
import { MyReducer } from './configs/reducer';
import { MyDispatchContext, MyUserContext } from './configs/context';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Login from './component/user/Login';
import { Icon, PaperProvider } from 'react-native-paper';
import signup from './component/user/Singup';
import Account from './component/user/account';
import BookTour from './component/tour/booktour.js';
import BookTourDetail from './component/tour/booktourdetail.js';
import News from './component/New/News.js';
import NewsDetail from './component/New/NewsDetail.js';
import Calendar from './component/Alert/Calendar.js';
import Logout from './component/user/Logout.js';
import MyStyle from './styles/MyStyle.js';



const Stack = createNativeStackNavigator();

const MyStack = () => {
  return (
    <Stack.Navigator>
      <Stack.Screen name='tour' component={Tour} options={{title: 'Chuyến đi'}} />
      <Stack.Screen name='tourdetail' component={TourDetail} options={{title: 'Chi tiết chuyến đi'}} />
      <Stack.Screen name='booktour' component={BookTour} options={{title: 'Đặt chuyến đi'}} />
      <Stack.Screen name='newsdetail' component={NewsDetail} options={{title: 'Chi tiết tin tức'}} />
    </Stack.Navigator>
  );
}

const Tab = createBottomTabNavigator();


const MyTab = () => {
  const user = useContext(MyUserContext); 

  return (
    <Tab.Navigator>
      <Tab.Screen name="Home" component={MyStack} options={{ title: "", tabBarIcon: () => <Icon size={30} color="black" source="airplane-takeoff" />}} />
      {user === null?<>
        <Tab.Screen name="Singup" component={signup} options={{ title: "Đăng ký", tabBarIcon: () => <Icon size={30} color="black" source="tree" />}} />
        <Tab.Screen name="Login" component={Login} options={{title: "Đăng nhập", tabBarIcon: () => <Icon size={30} color="black" source="login" />}} />
        <Tab.Screen name="News" component={News} options={{title: "Tin tức", tabBarIcon: () => <Icon size={30} color="black" source="newspaper-variant-multiple-outline" />}} />
      </>:<>
        <Tab.Screen name="Account" component={Account} options={{ title: "Tài khoản", tabBarIcon: () => <Icon size={30} color="black" source="account" />}} />
        <Tab.Screen name="MyTour" component={BookTourDetail} options={{ title: "Chuyến đi của tôi", tabBarIcon: () => <Icon size={30} color="black" source="ticket-account" />}} />
        
      </>
}
    </Tab.Navigator>
      
  );
}


export default function App() {
  const [user, dispatch]= useReducer(MyReducer, null)
  return (
    <NavigationContainer>
      <MyUserContext.Provider value={user}>
      <PaperProvider>
        <MyDispatchContext.Provider value={dispatch}>
          <MyTab/>
        </MyDispatchContext.Provider>
        </PaperProvider>
      </MyUserContext.Provider>
    </NavigationContainer>
  );
}

