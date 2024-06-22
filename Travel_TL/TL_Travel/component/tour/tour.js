import { ImageBackground, RefreshControl, SafeAreaView, ScrollView, TouchableOpacity, View } from "react-native"
import MyStyle from "../../styles/MyStyle"
import { ActivityIndicator, Button, Card, Chip, DataTable, Searchbar, SegmentedButtons, Text } from "react-native-paper"
import React, { useState } from "react"
import APIs, { endpoints } from "../../configs/APIs"
import moment from "moment"
import DateTimePicker from '@react-native-community/datetimepicker';

import Icon from "react-native-vector-icons/FontAwesome6"
import { isCloseToBottom } from "../Utils/util"
import StyleTour from "./StyleTour"
import Calendar from "../Alert/Calendar"
import StyleCal from "../Alert/StyleforCal"
import { Image } from "react-native"









const Tour =({navigation}) =>
    {
        const [tour,setTour]=React.useState([]);
        const [DeparturePlace, setDeparturePlace] = React.useState("");
        const [page, setPage]= React.useState(1);
        const [Destination, setDestination] = React.useState("");
        const [DepartureTime, setDepartureTime] = React.useState("");
        const [price, setPrice] = React.useState("");
        const [loading, setLoading] = React.useState(false);

    const loadTour = async () => {
        if (page > 0) {
            let url = `${endpoints['tour']}?noidi=${DeparturePlace}&noiden=${Destination}&thoigiandi=${DepartureTime}&Price=${price}&page=${page}`;
            try {
                setLoading(true);
                let res = await APIs.get(url);
                
               
                if (page === 1) 
                    {setTour(res.data.results) 
                    console.info(res.data.results)}
                else if (page > 1)
                    setTour(current => {
                        return [...current, ...res.data.results]
                    });
                // if (res.data.count === null) 
                //     console.log("không tìm thấy") 
                //     setPage(0);
            } catch (ex) {
                console.error(ex);
            } finally {
                setLoading(false);
            }
        }
    }

        React.useEffect(()=>{
             loadTour();
            },[DeparturePlace,DepartureTime,Destination, page, price]);


        
        
            const loadMore = ({nativeEvent}) => {
                if (loading===false && isCloseToBottom(nativeEvent)) {
                    console.log(page);
                    setPage(parseInt(page) + 1);
                    console.log(parseInt(page)+1);
                    console.log(page);
                }
            }
            const [value, setValue] = React.useState('Destination');
            const [q, setQ] = React.useState('');

            const search = (value, callback) => {
                setPage(1);
                callback(value);
                setQ(value);
            }


            const items = [1, 2, 3, 4, 5,6,7];

               
            
            //const [loading1, setLoading1] = useState(true);
            // const images = [
            //     'https://picsum.photos/300/200',
            //     'https://picsum.photos/700',
                
                
            //   ];
            // //const randomIndex = Math.floor(Math.random() * images.length)
            // const [currentIndex, setCurrentIndex] = useState(0);
        return(

        <View style={MyStyle.container}>
            <RefreshControl onRefresh={() => loadTour()} />
            <ScrollView onScroll={loadMore}>
            <Text style={MyStyle.tourspage}> Where do you like to go ?</Text>
            <View>
                <Searchbar style={MyStyle.sear} value={q} placeholder="Tìm chuyến đi..." onChangeText={t => value==='Destination'?search(t, setDestination):value==='DeparturePlace'?search(t, setDeparturePlace):search(t, setPrice)} />
                
                <SegmentedButtons 
                    style={MyStyle.sty}
                    density="small"
                    color={'white'}
                    value={value}
                    onValueChange={t=> {setValue(t);setQ("")}}
                    buttons={[
                    {
                        value:'Destination',
                        label: 'Nơi đến',
                        icon:'bus-side'
                        
                    },
                    {
                        value: 'DeparturePlace',
                        label: 'Nơi đi',
                        icon:'home-outline'
                    },
                    {   value: 'Price', 
                        label: 'Giá' ,
                        icon:'cash-100'
                    },
                    ]}
                />
            </View>
            <View>
                <Calendar></Calendar>
            </View>
            
            
            {loading ? <ActivityIndicator/>:<>
                {tour.map(c=> 
                <Card mode="elevated" style={MyStyle.card} key={c.id}> 
                    <Card.Content>
                    <Text style={MyStyle.text1}>{c.Id_Tour}</Text>
                    <Text style={MyStyle.text}>{c.Tour_Name}</Text>
                    </Card.Content>
                    {loading && <ActivityIndicator />}
                    <Card.Cover style={MyStyle.imgincard} source={{ uri: 'https://picsum.photos/600' }}/>
                    <View>
                     
                    {/* <Card.Cover
                            source={{ uri: images[currentIndex] }}
                            onLoad={() => {
                                const randomIndex = Math.floor(Math.random() * images.length);
                                setCurrentIndex(randomIndex);}}>
                    </Card.Cover> */}
                    </View>
                    <Text style={MyStyle.text2}>Ngày đăng: {moment(c.DatePost).fromNow()}</Text>
                    <Card.Actions>
                    <TouchableOpacity onPress={()=>navigation.navigate("tourdetail",{'tour_id':c.id})} key={c.id}><Text style={MyStyle.icon}><Icon color="#153050" size={20} name="mountain-sun"></Icon>  Xem thêm</Text></TouchableOpacity>
                    </Card.Actions>
                </Card>)}
            </>}   
           <View style={{ flexDirection: 'row' }}>
               { items.map((item) => <Button title="a"></Button>)}
           </View>
            </ScrollView>
        </View>
        
        );
    }
    

export default Tour;