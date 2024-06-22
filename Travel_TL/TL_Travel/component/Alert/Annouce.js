
import * as React from 'react';
import { View } from 'react-native';
import { Modal, Portal, Text, Button, PaperProvider } from 'react-native-paper';

const MyComponent = () => {
  const [visible, setVisible] = React.useState(false);

  const showModal = () => setVisible(true);
  const hideModal = () => setVisible(false);
  const containerStyle = {backgroundColor: 'white', padding: 20};
  

  return (
    <View>
      <Portal>
        <Modal visible={visible} onDismiss={hideModal} contentContainerStyle={containerStyle}>
          <Text>Bạn đã đặt chuyến đi thành công. Hãy thanh toán trước 24h để được xác nhận ! </Text>
        </Modal>
      </Portal>
      <Button style={{marginTop: 30}} onPress={showModal}>
        Đặt chuyến đi
      </Button>
    </View>
      
  );
};

export default MyComponent;