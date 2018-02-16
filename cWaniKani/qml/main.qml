import QtQuick 2.7
import QtQuick.Layouts 1.3
import QtQuick.Controls 1.4
import QtQuick.Window 2.2

ApplicationWindow {
    id: window
    visible: true
    width: Screen.width
    height: Screen.height

    menuBar: MenuBar {
        Menu {
            title: "File"
            MenuItem { text: "Open..." }
            MenuItem { text: "Close" }
        }

        Menu {
            title: "Edit"
            MenuItem { text: "Cut" }
            MenuItem { text: "Copy" }
            MenuItem { text: "Paste" }
        }
    }

    RowLayout {
        id: layout
        anchors.horizontalCenter: parent.horizontalCenter
        spacing: 6
        Rectangle {
            color: 'pink'
            Layout.fillWidth: false
            Layout.preferredWidth: 150
            Layout.preferredHeight: 150
            Text {
                id: apprenticeText
                anchors.centerIn: parent
                text: 'Apprentice'
            }
        }
        Rectangle {
            color: 'purple'
            Layout.fillWidth: false
            Layout.preferredWidth: 150
            Layout.preferredHeight: 150
            Text {
                id: guruText
                anchors.centerIn: parent
                text: 'Guru'
            }
        }
        Rectangle {
            color: 'blue'
            Layout.fillWidth: false
            Layout.preferredWidth: 150
            Layout.preferredHeight: 150
            Text {
                id: masterText
                anchors.centerIn: parent
                text: 'Master'
            }
        }
        Rectangle {
            color: 'light blue'
            Layout.fillWidth: false
            Layout.preferredWidth: 150
            Layout.preferredHeight: 150
            Text {
                id: enlightenedText
                anchors.centerIn: parent
                text: 'Enlightened'
            }
        }
        Rectangle {
            color: 'yellow'
            Layout.fillWidth: false
            Layout.preferredWidth: 150
            Layout.preferredHeight: 150
            Text {
                id: burnedText
                anchors.centerIn: parent
                text: 'Burned'
            }
        }
    }

    statusBar: StatusBar {
        RowLayout {
            anchors.fill: parent
            Label { text: "Read Only" }
        }
    }
}